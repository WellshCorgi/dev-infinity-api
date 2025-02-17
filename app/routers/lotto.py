import logging

from fastapi import APIRouter, Query, HTTPException
from app.core.lotto_generate import generate_num, get_lotto_winning_number
import datetime

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/lotto", tags=["lotto"])
@router.get("/gen")
async def generate_lotto(
        sets: int = Query(1, ge=1, le=5)
                    ):
    """로또 번호 생성 API"""
    try:
        results = [
            {"numbers": numbers, "bonus": bonus}
            for numbers, bonus in (generate_num() for _ in range(sets))
        ]
    except Exception as e:
        logger.error(f"Error generating lotto numbers: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

    try:
        latest_results = get_lotto_winning_number(None)
    except Exception as e:
        logger.error(f"Error retrieving latest lotto results: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve latest results")

    response = {
        "message": "Lotto numbers generated successfully",
        "timestamp": datetime.datetime.now().isoformat(),
        "generated_numbers": results,
        "latest_draw": latest_results
    }

    logger.info(f"Generated {sets} sets of lotto numbers")
    return response

@router.get("/search")
async def get_lotto_winning_number_result(round_num: int = None):
    """특정 회차의 로또 당첨 번호 조회 API"""
    try:
        latest_results = get_lotto_winning_number(round_num)
        if not latest_results:
            raise HTTPException(status_code=404, detail="Lotto results not found")

        return latest_results
    except Exception as e:
        logger.error(f"Error retrieving lotto results for round {round_num}: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve lotto results")