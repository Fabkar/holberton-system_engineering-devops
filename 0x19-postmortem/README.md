## 0x19-postmortem

Leonisa is a Colombia-based global company that manufactures and sells women's lingerie,
shapewear, swimwear, men's underwear, and activewear for both men and women.
This Postmortem case occurred before at Mother's Day a May 9 2020 on the virtual platform where sales during and after the pandemic have been growing exponentially.

<div align="center"><img src="https://prensaeventos.cl/wp-content/uploads/2019/11/leonisa-abre-su-tienda-mas-iconica-siguiendo-el-modelo-internacional.jpg"></div>

## Issue Summary
Mother's Day is a special date and perfect to lunch the amazing pomotion to increase sales, the design deparment with team developers have all ready to lunch a promotion with a great rebate the 50%, These announcements are normally left ready 2 or 3 days in advance, with the server scheduled to enable the publication just at hour 0:00 of the launch day.
An invalid configuration or human mistake changes the launch hour one day before launch.

## Timeline

00:35 AM - the virtual platform receives a request for a purchase.

00:48 AM - The system report the first call to costumer services.
  .
  .	 - The virtual platform continue receives more complaints.
  .
08:00 AM - There were about 265 complaints from people who could make a claim for the page.

08:03 AM - The marketing team sends authorization for the platform to be enabled as soon as possible.

08:05 AM - The webpage display the mother's day promotion (one day before launch).

08:10 AM - 50% of the Costumer sevice is dedicated to returning calls and emails to disadvantaged customers.

<div align="center"><img src="https://www.ambitojuridico.com/sites/default/files/reunion-socios-juntafreepik1.jpg"></div>

## Corrective/Preventive measures.
Leonisa should not stop or remove the publications because this can bring her legal problems with
the clients in addition to incurring in misleading advertising because the clients made their purchase and at the time of payment the system did not make the published discount.
- In these cases, the promotion must be enabled as soon as possible and continue its normal course.
- This issue could have been prevented by a simple checklist by the programmer that indicated to the servers a wrong time.
- It's necessary report and sends confirmation to managers of deparments of those important steps.
- The customer service contacted customers to refund the overcharged money.

Leonisa is committed to continually and quickly improving our technology and operational processes to prevent these inconvenients. We appreciate your patience and again apologize for the impact to you, your users, and your organization. We thank you for your business and continued support.