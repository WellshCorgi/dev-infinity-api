import logging
import random
import requests

logger = logging.getLogger(__name__)

def generate_num():
    numbers = random.sample(range(1, 45), 6)
    numbers.sort()
    bonus = random.choice([num for num in range(1, 46) if num not in numbers])
    return numbers, bonus


def get_lotto_winning_number(round_num: int = None):
    """특정 회차의 로또 당첨 번호를 가져오는 함수. 디폴트값은 최신 당첨 번호"""
    try:
        if round_num is None:
            # 파라미터 없이 넘어올때
            lotto_main_page = requests.get("https://dhlottery.co.kr/common.do?method=main").text
            latest_draw = int(lotto_main_page.split('<strong id="lottoDrwNo">')[1].split('</strong>')[0])

            response = requests.get(f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={latest_draw}")
            data = response.json()

            if data["returnValue"] != "success":
                raise Exception("Failed to fetch latest winning number")

            latest_numbers = [data[f"drwtNo{i}"] for i in range(1, 7)]
            bonus_number = data["bnusNo"]

            return {
                "draw_no": latest_draw,
                "draw_date": data["drwNoDate"],
                "numbers": latest_numbers,
                "bonus": bonus_number
            }
        else:
            # 특정 회차 조회
            response = requests.get(f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={round_num}")
            data = response.json()

            if data["returnValue"] == "success":
                latest_numbers = [data[f"drwtNo{i}"] for i in range(1, 7)]
                bonus_number = data["bnusNo"]
                return {
                    "draw_no": round_num,
                    "draw_date": data["drwNoDate"],
                    "numbers": latest_numbers,
                    "bonus": bonus_number
                }
            else:
                raise Exception(f"Could not find results for round {round_num}")
    except Exception as e:
        logger.error(f"Error fetching lotto results for round {round_num}: {str(e)}")
        return None