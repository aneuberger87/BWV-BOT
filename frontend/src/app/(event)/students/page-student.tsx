import { CardData } from "@/components/custom/card-data";
import {
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { getAllStudents } from "@/lib/fetches";

const LazyTableBodyStudent = async () => {
  const students = await getAllStudents();
  const timeSlots = ["A", "B", "C", "D", "E"];

  return (
    <TableBody>
      {students?.student.map((student, i) => (
        <TableRow key={i}>
          <TableCell contentEditable className="font-medium">
            {student.prename}
          </TableCell>
          <TableCell contentEditable>{student.surname}</TableCell>
          <TableCell contentEditable>{student.schoolClass}</TableCell>
          {timeSlots.map((timeSlot, i) => (
            <TableCell
              key={timeSlot}
              className={
                "text-right " +
                (student?.wishList?.[i]?.compId == -1
                  ? "font-bold text-red-500"
                  : "")
              }
            >
              {!!student.wishList[i] &&
                student.wishList[i].compId + " " + student.wishList[i].timeSlot}
            </TableCell>
          ))}
        </TableRow>
      ))}
    </TableBody>
  );
};

export const PageStudent = () => {
  return (
    <CardData
      table={{
        header: (
          <TableHeader>
            <TableRow>
              <TableHead className="w-[100px]">Vorname</TableHead>
              <TableHead>Nachname</TableHead>
              <TableHead>Klasse</TableHead>
              <TableHead className="text-right">W.1</TableHead>
              <TableHead className="text-right">W.2</TableHead>
              <TableHead className="text-right">W.3</TableHead>
              <TableHead className="text-right">W.4</TableHead>
              <TableHead className="text-right">W.5</TableHead>
            </TableRow>
          </TableHeader>
        ),
        body: <LazyTableBodyStudent />,
      }}
      title="Schüler"
      type="studentsList"
    />
  );
};
