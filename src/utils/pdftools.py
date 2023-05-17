from fpdf import FPDF
from datetime import datetime


class PdfTools(FPDF):

    PDF_SHEETS_CONFIG = {
        'orientation': 'P',
        'unit': 'mm',
        'format': 'A4'
    }
    
    PDF_HEADER = {
        'logo': './src/assets/img/logo-03.jpg',
        'title': 'Reporte',
        ''
    }

    def pdf_header(self) -> None:
        self.image('./src/assets/img/logo-03.jpg',
                   x=10, y=10, w=30, h=30)
        self.set_font('Arial', '', size=12)

        # tfont_size(self, 25)
        self.cell(w=0, h=0, txt='Reporte',
                  border=1, ln=1, align='C', fill=0)

        # tfont_size(self, 10)
        self.cell(w=0, h=10, txt='Generado el '+str(
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            border=1, ln=2, align='C', fill=0)
        self.ln(5)

    def pdf_body(self, section_pdf_main: dict):
        self.section_pdf_main(section_pdf_main['graph'],
                              section_pdf_main['title'],
                              section_pdf_main['description'])

    def section_pdf_main(self, graph: str, title: str,
                         description: str = ''):
        self.set_font('Arial', '', size=11)

        # tfont_size(self, 25)
        self.cell(w=0, h=10, txt=title,
                  border=1, ln=1, align='C', fill=0)

        self.image(graph, x=10, y=40, w=150, h=300)

        self.cell(w=0, h=0, txt=description,
                  border=1, ln=1, align='C', fill=0)


pdf = PdfTools(orientation='P', unit='mm', format='A4')
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Arial', '', 15)
pdf.pdf_header()
pdf.pdf_body({'graph': 'src/assets/img/imgcaja-bigote.png',
             'title': 'Diagrama de caja y bigote',
              'description': ''})

pdf.output('src/temp/prueba.pdf')
