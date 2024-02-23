import { UploadInline } from "@/components/custom/upload-inline";
import { Card, CardContent } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { getAllDummyStudentsWithWishes } from "@/lib/fetches";

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
          {timeSlots.map((timeSlot, i) => (
            <TableCell key={timeSlot} className="text-right">
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
    <Card className="h-full">
      <CardContent className="p-6 grid grid-rows-[auto_auto_auto_1fr] gap-4 h-full">
        <UploadInline label="Schüler Excel hochladen" id="student-excel" />
        <Separator />
        <Label>Schülerliste</Label>
        <ScrollArea className="min-h-full h-0">
          <Table>
            <TableCaption>A list of your recent invoices.</TableCaption>
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
            <LazyTableBodyStudent />
            {/* <TableFooter>
              <TableRow>
              </TableRow>
            </TableFooter> */}
          </Table>
        </ScrollArea>
      </CardContent>
    </Card>
  );
};
