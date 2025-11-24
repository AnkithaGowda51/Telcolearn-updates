                # Step 1: Define sample data (latency values in ms)
                latency_data = [20, 35, 50, 15, 40, 60, 25]


                # Step 2: Function to calculate average
                def calculate_average(data):
                    return sum(data) / len(data)


                # Step 3: Function to get summary (min, max, average)
                def get_summary(data):
                    summary = {
                        "Min": min(data),
                        "Max": max(data),
                        "Average": calculate_average(data)
                    }
                    return summary


                # Step 4 & 5: Test the functions

                results = get_summary(latency_data)
                print("Latency Summary:")
                print(results)