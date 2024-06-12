from concurrent.futures import ProcessPoolExecutor
from loggers import logger

async def addition(data):
    with ProcessPoolExecutor() as executor:
        exe = executor.submit(sum_numbers, data)
        return exe.result()

def sum_numbers(data):
    logger.info(f"Calling fun sum_numbers")
    print(data)
    numbers = data.numbers
    total = []
    if len(numbers)>1:
        for lst in numbers:
            add = sum(lst)
            total.append(add)
    else:
        add = sum(numbers)
        total.append(add)

    print('total = ', total)
    return total

