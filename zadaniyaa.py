# 1
# import time
# from concurrent.futures import ThreadPoolExecutor
#
# def fast_operation(a, b):
#     result = a + b
#     print(f"Fast operation result: {result}")
#     return result
#
# def slow_operation(a):
#     time.sleep(a**2)
#     print("Slow operation complete")
#
# def main():
#     a = 3
#     b = 5
#
#     with ThreadPoolExecutor() as executor:
#
#         fast_future = executor.submit(fast_operation, a, b)
#
#         slow_future = executor.submit(slow_operation, a)
#
#         fast_result = fast_future.result()
#         slow_result = slow_future.result()
#
#         print("Both operations complete")
#
# if __name__ == "__main__":
#     main()
# 2
# import asyncio
#
# async def answer_phone_call():
#     print("Answering phone call")
#     await asyncio.sleep(3)
#
# async def greet_visitor():
#     print("Greeting visitor")
#     await asyncio.sleep(2)
#
# async def book_flight_tickets():
#     print("Booking flight tickets")
#     await asyncio.sleep(5)
#
# async def control_meeting_schedule():
#     print("Controlling meeting schedule")
#     await asyncio.sleep(4)
#
# async def fill_documents():
#     print("Filling documents")
#     await asyncio.sleep(6)
#
# async def secretary_tasks():
#     tasks = [
#         answer_phone_call(),
#         greet_visitor(),
#         book_flight_tickets(),
#         control_meeting_schedule(),
#         fill_documents(),
#     ]
#
#     await asyncio.gather(*tasks)
#
# if __name__ == "__main__":
#     asyncio.run(secretary_tasks())