import { CardData } from "@/components/custom/card-data";
import {
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { getAllCompanies } from "@/lib/fetches";

const LazyTableBodyCompany = async () => {
  const companies = await getAllCompanies();
  const timeSlots = ["A", "B", "C", "D", "E"];
  return (
    <TableBody>
      {companies.company.map((company, i) => (
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
                  ?.room?.roomId
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
    <CardData
      table={{
        header: (
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
        ),
        body: <LazyTableBodyCompany />,
      }}
      title="Firmen"
    />
  );
};
