desc = '''El diagrama de caja y bigote utilizado para representar los datos de calidad del vino proporciona una visión rápida y resumida de la distribución y dispersión de los datos, así como de posibles valores atípicos. Todos los siguientes gráficos están realizados en función de las variables más "relevantes."'''
desc_bar = '''Estos diagramas permitirán entender la relación importante que existe entre las variables "relevantes" y la calidad del vino, la cual esta ultima es la que ayudará a determinar si el vino es bueno o no. Por ejemplo, en la gráfica izquierda se observa que entre más acidez volátil menos calidad tendrá el vino, caso contrario con el acido cítrico.'''
desc_bar2 = '''Para los cloruros podemos afirmar que entre más haya peor será la calidad del vino, caso contrario con los sulfatos, pues se da a entender que entre más haya mejor será el vino.'''
desc_bar3 = '''En esta ultima gráfica se entiende que entre más alcohol tenga el vino mejor será la calidad, sin embargo, se puede ver que la cantidad debe ser moderada.'''
paragraph = '''Los siguientes datos fueron recopilados al momento de aplicar el algoritmo de predicción al set de datos:
Matriz de confusión: {}
Precisión del algoritmo: {}
F1 Score: {}
ROC Score: {}
Recall Score: {}

Clasifiación
Se determinó que un vino bueno es aquel que su calidad supere los 6.5.
Cantidad de vinos buenos: {}
Cantidad de vinos malos: {}

Valores unicos:
{}
{}
{}
{}
{}
{}'''

second_line = '<body><div class="es-wrapper-color"> <!--[if gte mso 9]><v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"> <v:fill type="tile" color="#fafafa"></v:fill> </v:background><![endif]--><table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0"><tr><td valign="top"><table cellpadding="0" cellspacing="0" class="es-content" align="center"><tr><td align="center"><table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600"><tr><td class="es-p20t es-p10b es-p20r es-p20l" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tr><td width="560" align="center" valign="top"><table cellpadding="0" cellspacing="0" width="100%" role="presentation"><tr><td align="center" class="es-p20t es-p5b es-m-txt-c"><h1>Notificación de recepción de correo</h1></td>'
forth_line = '</tr></table><table cellpadding="0" cellspacing="0" class="es-content" align="center"><tr><td align="center"><table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600"><tr><td class="es-p20t es-p20r es-p20l" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tr><td width="560" align="center" valign="top"><table cellpadding="0" cellspacing="0" width="100%" role="presentation"><tr><td align="center" class="es-m-txt-c"><h3>No responda a este correo por favor</h3></td></tr></table></td></tr></table></td></tr></table></td>'
fifth_line = '</tr></table><table cellpadding="0" cellspacing="0" class="es-content" align="center"><tr><td class="es-info-area" align="center"><table class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: transparent" bgcolor="rgba(0, 0, 0, 0)"><tr><td class="es-p20" align="left" bgcolor="#ffffff" style="background-color: #ffffff"><table cellpadding="0" cellspacing="0" width="100%"><tr><td width="560" align="center" valign="top"><table cellpadding="0" cellspacing="0" width="100%" role="presentation"><tr><td align="center" class="es-infoblock"><p><a target="_blank"></a>No longer want to receive these emails?&nbsp;<a href target="_blank">Unsubscribe</a>.<a target="_blank"></a></p></td></tr></table></td></tr></table></td></tr></table></td></tr></table></td></tr></table></div></body></html>'
email_we_to_user = str(second_line)+'''</tr><tr><td align="center" class="es-p10t es-p10b es-m-txt-c"><h3>Estimado/a <strong>usuario/a</strong>,<br>Enviado&nbsp;el&nbsp;<a target="_blank" style="text-decoration: none">{} <span style="color:#000000">a las </span><span style="color:#5c68e2">{}</span><span style="color:#000000"></span></a></h3></td></tr><tr><td align="center" class="es-p5t es-p5b"><p style="line-height: 120%">Le informamos con satisfacción que hemos recibido su correo electrónico con éxito.<br>Nos pondremos en contacto con usted a la brevedad posible.</p><p style="line-height: 120%">Si tiene alguna pregunta o inquietud, no dude en comunicarse con nosotros. Estamos aquí para ayudarle.</p><p style="line-height: 120%">.</p></td></tr></table></td></tr></table></td></tr></table></td>'''+str(forth_line)+str(fifth_line)
