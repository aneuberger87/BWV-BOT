import { UploadInline } from "@/components/custom/upload-inline";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
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
import { getAllCompanies } from "@/lib/fetches";
import { FaQuestion } from "react-icons/fa";

const LazyTableBodyCompany = async () => {
  const students = await getAllCompanies();
  const timeSlots = ["A", "B", "C", "D", "E"];

  return (
    <TableBody>
      {students.company.map((company, i) => (
        <TableRow key={i}>
          <TableCell className="font-medium">{company.id}</TableCell>
          <TableCell>{company.compName}</TableCell>
          <TableCell>{company.trainingOccupation}</TableCell>
          <TableCell className="text-right">
            {company.numberOfMembers}
          </TableCell>
          {timeSlots.map((timeSlot) => (
            <TableCell key={timeSlot} className="text-right">
              {
                company.meeting.find((meeting) => meeting.timeSlot === timeSlot)
                  ?.room
              }
            </TableCell>
          ))}
        </TableRow>
      ))}
    </TableBody>
  );
};

export const PageCompany = () => {
  return (
    <Card className="h-full">
      <CardContent className="p-6 grid grid-rows-[auto_auto_auto_1fr] gap-4 h-full">
        <UploadInline label="Firmen Excel hochladen" id="company-excel" />
        <Separator />
        <Label>Schülerliste</Label>
        <ScrollArea className="min-h-full h-0">
          <Table className="relative">
            <TableCaption>A list of your recent invoices.</TableCaption>
            <TableHeader>
              <TableRow>
                <TableHead className="w-[100px]">ID</TableHead>
                <TableHead>Name</TableHead>
                <TableHead>Fachrichtung</TableHead>
                <TableHead>Platz</TableHead>
                <TableHead className="text-right">A</TableHead>
                <TableHead className="text-right">B</TableHead>
                <TableHead className="text-right">C</TableHead>
                <TableHead className="text-right">D</TableHead>
                <TableHead className="text-right">E</TableHead>
              </TableRow>
            </TableHeader>
            <LazyTableBodyCompany />
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
