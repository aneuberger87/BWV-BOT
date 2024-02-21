import { UploadInline } from "@/components/custom/upload-inline";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Separator } from "@/components/ui/separator";
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { getAllDummyStudentsWithWishes } from "@/lib/fetches";
import { FaQuestion } from "react-icons/fa";

const LazyTableBodyStudent = async () => {
  const students = await getAllDummyStudentsWithWishes();
  const timeSlots = ["A", "B", "C", "D", "E"];

  return (
    <TableBody>
      {students.student.map((student, i) => (
        <TableRow key={i}>
          <TableCell className="font-medium">{student.prename}</TableCell>
          <TableCell>{student.surname}</TableCell>
          <TableCell>{student.schoolClass}</TableCell>
          {timeSlots.map((timeSlot) => (
            <TableCell key={timeSlot} className="text-right">
              {
                student.wishList.find((wish) => wish.timeSlot === timeSlot)
                  ?.compId
              }
            </TableCell>
          ))}
        </TableRow>
      ))}
    </TableBody>
  );
};

export const PageStudent = () => {
  return (
    <div>
      <Card>
        <CardContent className="p-6 flex flex-col gap-4">
          <UploadInline label="Schüler Excel hochladen" id="student-excel" />
          <Separator />
          <Label>Schülerliste</Label>
          <Table>
            <TableCaption>A list of your recent invoices.</TableCaption>
            <TableHeader>
              <TableRow>
                <TableHead className="w-[100px]">Vorname</TableHead>
                <TableHead>Nachname</TableHead>
                <TableHead>Klasse</TableHead>
                <TableHead className="text-right">A</TableHead>
                <TableHead className="text-right">B</TableHead>
                <TableHead className="text-right">C</TableHead>
                <TableHead className="text-right">D</TableHead>
                <TableHead className="text-right">E</TableHead>
              </TableRow>
            </TableHeader>
            <LazyTableBodyStudent />
            {/* <TableFooter>
              <TableRow>
              </TableRow>
            </TableFooter> */}
          </Table>
        </CardContent>
      </Card>
    </div>
  );
};
