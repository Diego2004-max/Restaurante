from django.http import HttpResponse
from reportlab.pdfgen import canvas
from orders.models import OrderItem

def top_dishes_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=top_dishes.pdf"

    pdf = canvas.Canvas(response)
    pdf.drawString(100, 800, "REPORTE: Platos más vendidos")

    y = 760
    ranking = (
        OrderItem.objects
        .values("dish__name")
        .order_by("-quantity")
        .annotate(total=models.Sum("quantity"))[:5]
    )

    for item in ranking:
        pdf.drawString(100, y, f"{item['dish__name']}: {item['total']} vendidos")
        y -= 20

    pdf.save()
    return response
