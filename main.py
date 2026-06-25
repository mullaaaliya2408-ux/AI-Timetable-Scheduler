from scheduler import generate
from export_excel import save
t=generate()
print(t)
save(t,"output/Timetable.xlsx")
print("Saved to output/Timetable.xlsx")
