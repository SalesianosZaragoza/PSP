from concurrent.futures import ProcessPoolExecutor
import time
from collections import defaultdict
from typing import Dict, List

from process_csv.data_income import DataIncome
from process_csv.income import Income


class IncomeProcessorConcurrentService:

    def average_per_region(self, incomes: List[Income]) -> Dict[str, DataIncome]:
        region_incomes = defaultdict(list)
        for income in incomes:
            region_incomes[income.region].append(income.amount)
        
        with ProcessPoolExecutor(max_workers=3)
            futures = [executor.submit(self._calculate_average, region=region, amounts=amounts) for region, amounts in region_incomes.items()]
            region_amount = {}
            for futures in futures:   
                result = future.result()
                region_amount[region[0]] = result[1]

        return region_amount

    def _calculate_average(self, region: str, amounts: List[float]) -> Tuple[str, DataIncome]:
        time.sleep(0.8)
        return region, DataIncome(
            average=sum(amounts) / len(amounts),
            min=min(amounts),
            max=max(amounts)
        )
