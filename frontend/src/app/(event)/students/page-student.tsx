import { CardData } from "@/components/custom/card-data";
import {
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { getDataStatusCachable } from "@/lib/data-status";
import { getAllStudents, getAllStudentsAllocation } from "@/lib/fetches";

const LazyTableBodyStudent = async (props: { asOutput?: boolean }) => {
  const students = props.asOutput
    ? await getAllStudentsAllocation()
    : await getAllStudents();
  const timeSlots = ["A", "B", "C", "D", "E"];
  const wishList = ["W1", "W2", "W3", "W4", "W5", "W6"];

  return (
    <TableBody>
      {students?.student.map((student, i) => (
        <TableRow key={i}>
          <TableCell className="w-max whitespace-nowrap font-medium">
            {student.prename}
          </TableCell>
          <TableCell>{student.surname}</TableCell>
          <TableCell>{student.schoolClass}</TableCell>
          {props.asOutput
            ? timeSlots.map((wish, i) => (
                <TableCell
                  key={i}
                  className={
                    "w-max px-2 text-right " +
                    (student?.wishList?.[i]?.compId == -1
                      ? "font-bold text-red-500"
                      : "")
                  }
                >
                  {!!student.wishList[i] &&
                    student.wishList[i].compId +
                      " " +
                      student.wishList[i].timeSlot}
                </TableCell>
              ))
            : wishList.map((timeSlot, i) => (
                <TableCell
                  key={timeSlot}
                  className={
                    "w-max px-2 text-right " +
                    (student?.wishList?.[i]?.compId == -1
                      ? "font-bold text-red-500"
                      : "")
                  }
                >
                  {!!student.wishList[i] &&
                    student.wishList[i].compId +
                      " " +
                      student.wishList[i].timeSlot}
                </TableCell>
              ))}
        </TableRow>
      ))}
    </TableBody>
  );
};

export const PageStudent = () => {
  const dataExists = getDataStatusCachable().output.calculated;
  return (
    <CardData
      tableOutput={
        dataExists
          ? {
              showDefault: true,
              header: (
                <TableHeader>
                  <TableRow>
                    <TableHead className="w-[100px]">Vorname</TableHead>
                    <TableHead>Nachname</TableHead>
                    <TableHead>Klasse</TableHead>
                    <TableHead className="w-max px-2 text-right ">A</TableHead>
                    <TableHead className="w-max px-2 text-right ">B</TableHead>
                    <TableHead className="w-max px-2 text-right ">C</TableHead>
                    <TableHead className="w-max px-2 text-right ">D</TableHead>
                    <TableHead className="w-max px-2 text-right ">E</TableHead>
                  </TableRow>
                </TableHeader>
              ),
              body: <LazyTableBodyStudent asOutput />,
            }
          : undefined
      }
      table={{
        header: (
          <TableHeader>
            <TableRow>
              <TableHead className="w-[100px]">Vorname</TableHead>
              <TableHead>Nachname</TableHead>
              <TableHead>Klasse</TableHead>
              <TableHead className="w-max px-2 text-right ">W1</TableHead>
              <TableHead className="w-max px-2 text-right ">W2</TableHead>
              <TableHead className="w-max px-2 text-right ">W3</TableHead>
              <TableHead className="w-max px-2 text-right ">W4</TableHead>
              <TableHead className="w-max px-2 text-right ">W5</TableHead>
              <TableHead className="w-max px-2 text-right ">W6</TableHead>
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
