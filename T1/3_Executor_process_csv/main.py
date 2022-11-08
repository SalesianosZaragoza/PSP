from datetime import datetime

from services.csv_service import CSVService
from services.income_processor_service import IncomeProcessorService
from services.income_processor_concurrent_service import IncomeProcessorConcurrentService
import os

if __name__ == '__main__':
    # 1. Read CSV file
    csv_service = CSVService()
    incomes = csv_service.read_csv(os.getcwd()+'/T1/3_Executor_process_csv/data.csv')
    # 2. Select income Processor
    income_processor = IncomeProcessorService()
    #income_processor = IncomeProcessorConcurrentService()

    # 3. Calculate average per region
    start_time = datetime.now()
    income_per_region = income_processor.average_per_region(incomes)
    end_time = datetime.now()

    # 4. Print results
    print(income_per_region)
    print(f'Duration: {end_time - start_time}')
