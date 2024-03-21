import { CardData } from "@/components/custom/card-data";
import {
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { getDataStatusCachable } from "@/lib/data-status";
import { getAllCompanies } from "@/lib/fetches";

const LazyTableBodyCompany = async (props: { type: "output" | "input" }) => {
  const companies = await getAllCompanies();
  const timeSlots = ["A", "B", "C", "D", "E"];
  return (
    <TableBody>
      {companies.company.map((company, i) => (
        <TableRow key={i}>
          <TableCell className="w-max font-medium">{company.id}</TableCell>
          <TableCell>{company.compName}</TableCell>
          <TableCell>{company.trainingOccupation}</TableCell>
          <TableCell className="text-right">
            {company.numberOfMembers}
          </TableCell>
          {props.type == "output"
            ? timeSlots.map((timeSlot) => (
                <TableCell
                  key={timeSlot}
                  className="text-right"
                  contentEditable
                  suppressContentEditableWarning
                >
                  {
                    company.meeting.find(
                      (meeting) => meeting.timeSlot === timeSlot,
                    )?.room?.roomId
                  }
                </TableCell>
              ))
            : null}
        </TableRow>
      ))}
    </TableBody>
  );
};

export const PageCompany = () => {
  const dataExists = getDataStatusCachable().output.calculated;
  return (
    <CardData
      table={{
        header: (
          <TableHeader>
            <TableRow>
              <TableHead className="w-max">ID</TableHead>
              <TableHead>Name</TableHead>
              <TableHead>Fachrichtung</TableHead>
              <TableHead>Platz</TableHead>
            </TableRow>
          </TableHeader>
        ),
        body: <LazyTableBodyCompany type="input" />,
      }}
      tableOutput={
        dataExists
          ? {
              showDefault: true,
              header: (
                <TableHeader>
                  <TableRow>
                    <TableHead className="w-max">ID</TableHead>
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
              body: <LazyTableBodyCompany type="output" />,
            }
          : undefined
      }
      title="Firmen"
      type="companiesList"
    />
  );
};
