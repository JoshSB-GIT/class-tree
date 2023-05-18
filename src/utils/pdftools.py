from fpdf import FPDF
from datetime import datetime


class PdfTools(FPDF):

    PDF_SHEETS_CONFIG = {
        'orientation': 'P',
        'unit': 'mm',
        'format': 'A4'
    }

    def header(self):
        """_summary_
        """
        now = datetime.now()
        # Logo
        self.image('./src/assets/img/logo-03.jpg', x=10, y=10, w=30)

        # Fuente y tamaño del texto
        self.set_font('Arial', 'B', 12)

        # Fecha de creación
        self.cell(0, 10,
                  txt="Fecha de creación: " +
                      str(now.strftime("%Y-%m-%d %H:%M:%S")),
                  align='R', ln=1)

        # Título del reporte
        self.set_font('Arial', 'B', 18)
        self.cell(0, 20, txt="Reporte del set de datos", align='C', ln=1)

    def footer(self):
        """_summary_
        """
        # Posicionar el footer a 1.5 cm del fondo de la página
        self.set_y(-15)

        # Establecer la fuente y el tamaño del texto del footer
        self.set_font('Arial', 'I', 10)

        # Número de página centrado
        self.cell(0, 10, 'Página {}'.format(self.page_no()), 0, 0, 'C')

    def img_grid_section(self, title: str = '', description: str = '',
                         image_paths: list = [], image_width: int = 80,
                         image_height: int = 80, nrows=2, ncols=2,
                         description2: str = '', descriptions_size: int = 12,
                         title_size: int = 16, spacing: int = 10):
        """_summary_

        Args:
            title (str, optional): _description_. Defaults to ''.
            description (str, optional): _description_. Defaults to ''.
            image_paths (list, optional): _description_. Defaults to [].
            image_width (int, optional): _description_. Defaults to 80.
            image_height (int, optional): _description_. Defaults to 80.
            nrows (int, optional): _description_. Defaults to 2.
            ncols (int, optional): _description_. Defaults to 2.
            description2 (str, optional): _description_. Defaults to ''.
            descriptions_size (int, optional): _description_. Defaults to 12.
            title_size (int, optional): _description_. Defaults to 16.
        """
        if title != '':  # Título centrado
            self.set_font('Arial', 'B', title_size)
            self.cell(0, 10, txt=title, align='C', ln=1)

        if description != '':
            # Descripción justificada
            self.set_font('Arial', '', descriptions_size)
            self.multi_cell(0, 5, txt=description, align='J')

            # Crear una tabla con 3 columnas
            self.set_font('Arial', '', descriptions_size)

        if len(image_paths) != 0:
            # Ajustar la posición y tamaño de las imágenes
            y_start = self.get_y() + 15
            # Posición vertical de inicio de las imágenes
            image_width = image_width
            image_height = image_height
            spacing = spacing  # Espacio entre las imágenes

            rows = nrows
            cols = ncols
            for row in range(rows):
                for col in range(cols):
                    index = row * cols + col
                    if index >= len(image_paths):
                        break

                    x = self.get_x() + col * (image_width + spacing)
                    y = y_start + row * (image_height + spacing)

                    self.image(image_paths[index], x=x, y=y,
                               w=image_width, h=image_height)
                    # print('index: ', index, 'row: ', row, 'col: ', col)
                    # print('x: ', x, 'y: ', y, 'getx: ', self.get_x())

            # Espacio adicional después de las imágenes
            self.ln((image_height + spacing) * rows + 10)

        if description2 != '':
            # Descripción justificada
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 5, txt=description2, align='J')

    def simple_section(self, title: str = '', description2: str = '',
                       description: str = '', image_path: str = '',
                       image_width: int = 80, image_height: int = 80,
                       descriptions_size: int = 12,
                       title_size: int = 16):
        """_summary_

        Args:
            title (str, optional): _description_. Defaults to ''.
            description2 (str, optional): _description_. Defaults to ''.
            description (str, optional): _description_. Defaults to ''.
            image_path (str, optional): _description_. Defaults to ''.
            image_width (int, optional): _description_. Defaults to 80.
            image_height (int, optional): _description_. Defaults to 80.
            descriptions_size (int, optional): _description_. Defaults to 12.
            title_size (int, optional): _description_. Defaults to 16.
        """
        # Título centrado
        if title != '':
            self.set_font('Arial', 'B', title_size)
            self.cell(0, 10, txt=title, align='C', ln=1)
        if description != '':
            # Descripción justificada
            self.set_font('Arial', '', descriptions_size)
            self.multi_cell(0, 10, txt=description, align='J')

        if image_path != '':
            # Imagen centrada
            image_width = 100
            image_height = 100
            x = self.get_x() + (self.w - image_width) / 2
            y = self.get_y() + 10
            self.image(image_path, x=x, y=y, w=image_width, h=image_height)

            self.ln(image_height + 20)

        if description2 != '':
            # Descripción justificada
            self.set_font('Arial', '', descriptions_size)
            self.multi_cell(0, 10, txt=description2, align='J')

    def text_section(self, title: str = '', paragraph: str = '',
                     title_size: int = 16, paragraph_size: int = 12):
        """_summary_

        Args:
            title (str, optional): _description_. Defaults to ''.
            paragraph (str, optional): _description_. Defaults to ''.
            title_size (int, optional): _description_. Defaults to 16.
            paragraph_size (int, optional): _description_. Defaults to 12.
        """
        # Título centrado
        if title != '':
            self.set_font('Arial', 'B', title_size)
            self.cell(0, 10, txt=title, align='C', ln=1)

        # Párrafo justificado con saltos de línea y espacios
        if paragraph != '':
            self.set_font('Arial', '', paragraph_size)
            self.multi_cell(0, 10, txt=paragraph, align='J')


# pdf = PdfTools(orientation='P', unit='mm', format='A4')
# pdf.add_page()
# pdf.output('./src/temp/prueba.pdf')
