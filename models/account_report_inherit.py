from odoo import models
import io
import base64
import xlsxwriter

class JournalReportCustomHandler(models.AbstractModel):
    _inherit = "account.journal.report.handler"

    def export_to_xlsx(self, options, response=None):
        """Custom XLSX export for Journal Audit with header."""
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet("Journal Audit")

        # Custom header
        company = self.env.company
        sheet.write(0, 0, f"Company Name: {company.name}")
        sheet.write(1, 0, f"VAT No.: {company.vat or ''}")
        sheet.write(2, 0, f"Address: {company.partner_id.contact_address or ''}")
        sheet.write(3, 0, f"Period Covered: {options.get('date', {}).get('string', '')}")

        # TODO: dump Odoo’s journal lines starting row 5

        workbook.close()
        output.seek(0)
        data = output.read()

        if response is not None:
            # XLSX button case → write directly
            response.stream.write(data)
            return None
        else:
            # Programmatic call case → return dict
            return {
                'file_name': "custom_journal_audit.xlsx",
                'file_content': data,
                'file_type': 'xlsx',
            }
      