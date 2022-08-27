from PyPDF2 import PdfFileMerger

#pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

pdfs = ['My_JustFly_Reservation.pdf', 'Travel_Itinerary_to_Canada_v3.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("My_JustFly_Reservation_and_travel_itinerary_v2.pdf")
merger.close()
