from django.core.management import BaseCommand, call_command
from stock_archive.models import*
import csv
import xlrd

class Command(BaseCommand):
    help = "DEV COMMAND: Fill databasse with a set of data for testing purposes"

    def handle(self, *args, **options):
        workbook = xlrd.open_workbook("stock/company_details.xlsx")
        worksheet = workbook.sheet_by_index(0)
        offset = 1
        rows = []
        for i, row in enumerate(range(worksheet.nrows)):
            if i <= offset: #skip headers
                continue
            r = []
            for j, col in enumerate(range(worksheet.ncols)):
                r.append(worksheet.cell_value(i, j))
            rows.append(r)
        for row in rows:
            print(row)
            company_details, created = CompanyDetail.objects.get_or_create(
                symbol = row[0],
                name = row[1],
                market_cap = float(row[2]),
                sector = row[3],
                industry = row[4]
            )
            company_details.save()


        with open("stock/company_data.csv") as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if not index:
                    continue
                else:
                    print(row)
                    company, created = Company.objects.get_or_create(
                        date = row[0],
                        symbol = row[1],
                        open_cost = float(row[2]),
                        close_cost = float(row[3]),
                        low_cost = float(row[4]),
                        high_cost = float(row[5]),
                        volume_cost = float(row[6])
                    )
                    company.save()

