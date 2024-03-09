from bs4 import BeautifulSoup


def modify_html_style(input_html):
    soup = BeautifulSoup(input_html, 'html.parser')

    for tag in soup.find_all(style=True):
        # style_tag = tag['style']
        # if 'font-size' in style_tag and 'font-family' not in style_tag:
        #     tag['style'] = style_tag + '; font-family: Arial, sans-serif;'
        # if 'font-size' not in style_tag and 'font-family' in style_tag:
        #     tag['style'] = style_tag + '; font-size: 12px;'
        #
        # print(f"{tag['style'] = }")
        styles = tag['style'].split(';')

        modified_styles = []

        for style in styles:
            if ':' in style:
                key, value = style.split(':', 1)
                key = key.strip()
                value = value.strip()

                if key == 'font-size' and 'px' in value:
                    print(f"{key = } {value = }")
                    font_size = float(value.replace('px', ''))
                    if 0 <= font_size <= 16:
                        value = '12px'
                elif key == 'font-family':
                    print(f"{key = } {value = }")
                    if value != 'Arial, sans-serif':
                        value = 'Arial, sans-serif'

                modified_styles.append(f'{key}: {value}')

        tag['style'] = '; '.join(modified_styles)

        for div_tag in soup.find_all('div', style=None):
            # Додаємо новий стиль до тегу div
            div_tag['style'] = 'font-size: 12px; font-family: Arial, sans-serif;'

    return str(soup)


# Приклад використання:
input_html = '<p style="font-size: 10px; font-family: &quot;Lucida Grande&quot;, Helvetica, Verdana, Arial, sans-serif;">Hello, World!</p>'
# body_html_1 = '<div>\n<div itemscope="itemscope" itemtype="http://schema.org/EmailMessage">\n    <div itemprop="potentialAction" itemscope="itemscope" itemtype="http://schema.org/ViewAction">\n        <link itemprop="target" href="https://redirect-url.email/?link=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.lead%26res_id%3D23866&amp;apn=com.odoo.mobile&amp;afl=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.lead%26res_id%3D23866&amp;ibi=com.odoo.mobile&amp;ifl=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.lead%26res_id%3D23866"/>\n        <link itemprop="url" href="https://redirect-url.email/?link=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.lead%26res_id%3D23866&amp;apn=com.odoo.mobile&amp;afl=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.lead%26res_id%3D23866&amp;ibi=com.odoo.mobile&amp;ifl=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.lead%26res_id%3D23866"/>\n        <meta itemprop="name" content="View Lead/Opportunity"/>\n    </div>\n</div>\n<div summary="o_mail_notification" style="padding: 0px; width:600px;">\n    <table cellspacing="0" cellpadding="0" border="0" style="width: 600px; margin-top: 5px;">\n    <tbody><tr>\n    <td valign="center">\n        <a style="padding: 8px 12px; font-size: 12px; color: #FFFFFF; text-decoration: none !important; font-weight: 400; background-color: #875A7B; border: 0px solid #875A7B; border-radius:3px" href="https://redirect-url.email/?link=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.lead%26res_id%3D23866&amp;apn=com.odoo.mobile&amp;afl=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.lead%26res_id%3D23866&amp;ibi=com.odoo.mobile&amp;ifl=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.lead%26res_id%3D23866">\n            View Lead/Opportunity\n        </a>\n                |\n                <a style="color: #875A7B; text-decoration:none !important;" href="http://localhost:8069/lead/convert?res_id=23866&amp;token=c707dcc7435b3badc4ea9d4d0dc44cc45c1b7be3">\n                    Convert to opportunity\n                </a>\n                |\n                <a style="color: #875A7B; text-decoration:none !important;" href="https://redirect-url.email/?link=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.team%26res_id%3D1&amp;apn=com.odoo.mobile&amp;afl=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.team%26res_id%3D1&amp;ibi=com.odoo.mobile&amp;ifl=http%3A%2F%2Flocalhost%3A8069%2Fmail%2Fview%3Fmodel%3Dcrm.team%26res_id%3D1">\n                    Sales Team Settings\n                </a>\n    </td>\n    <td valign="center" align="right">\n        <img style="padding: 0px; margin: 0px; height: auto; max-width: 200px; max-height: 36px;" src="http://localhost:8069/logo.png?company=1" alt="Bluesky (UK) Limited" loading="lazy"/>\n    </td>\n    </tr><tr>\n    <td colspan="2" style="text-align:center;">\n        <hr width="100%" style="background-color:rgb(204,204,204);border:medium none;clear:both;display:block;font-size:0px;min-height:1px;line-height:0; margin:4px 0 12px 0;"/>\n    </td>\n    </tr></tbody>\n    </table>\n</div>\n<div><p>111</p></div>\n<div style="font-size: 13px;"><p style="margin:0px 0 12px 0;box-sizing:border-box;line-height:inherit;font-weight:inherit;font-size:12px;font-family:Arial, sans-serif;">Kind\n    Regards</p><p style="margin:0px 0 12px 0;box-sizing:border-box;line-height:inherit;font-weight:inherit;font-size:12px;font-family:Arial, sans-serif;">\n    <span style="box-sizing:border-box;line-height:inherit;font-size:12px;font-family:Arial, sans-serif;font-weight: bolder">Wojciech Betyna | Systems &amp; IT Manager<br><img class="img-fluid" src="https://portal.blueskysolutionsuk.com/web/image/470780-01ce802f/Updated Email footer from 9th Sept.jpg?access_token=3ad4d026-a008-406b-9882-330e5d480cdd" width="911" style="border-style:none;box-sizing:border-box;max-width:100%;vertical-align:middle;width: 911px; height: 166px; mso-hide: all; mso-hide: all; mso-hide: all; mso-hide: all; mso-hide: all; mso-hide: all; mso-hide: all;" height="166"><!--<![endif]--><!--<![endif]--><!--<![endif]--><!--<![endif]--><!--<![endif]-->\n        <!--<![endif]--><!--<![endif]--></span></p><p style="margin:0px 0 12px 0;box-sizing:border-box;line-height:inherit;font-weight:inherit;font-size:12px;font-family:Arial, sans-serif;">\n    Visit: www.blueskysolutionsuk.com\xa0<br>Call: +44 (0) 1472 240940\xa0<br>Email: sales@blueskysolutionsuk.com\n</p><p style="margin:0px 0 12px 0;box-sizing:border-box;line-height:inherit;font-weight:inherit;font-size:12px;font-family:Arial, sans-serif;">\n    Address: Bluesky (UK) Ltd, Horizon House, Estate Road Five, Grimsby, North East Lincolnshire, DN31 2TG\xa0</p></div>\n </div>'
modified_html = modify_html_style(input_html)
print(f"{modified_html = }")
