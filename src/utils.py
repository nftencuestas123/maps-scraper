import csv
def export_results(results, formato="csv"):
    if formato == "csv":
        with open("results.csv", "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            for r in results:
                writer.writerow(r)
