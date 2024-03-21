import { CardData } from "@/components/custom/card-data";
import {
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { getDataStatusCachable } from "@/lib/data-status";
import { getAllCompanies, getAllRooms } from "@/lib/fetches";
import { EditableCell } from "./editable-cell";
import { FaTimes } from "react-icons/fa";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { Fragment } from "react";

const LazyTableBodyCompany = async (props: { type: "output" | "input" }) => {
  const [companies, rooms] = await Promise.all([
    getAllCompanies(),
    getAllRooms(),
  ]);
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
            ? timeSlots.map((timeSlot, i) => {
                const meeting = company.meeting.find(
                  (meeting) => meeting.timeSlot === timeSlot,
                );
                return (
                  <Fragment key={i}>
                    {!!meeting ? (
                      <EditableCell
                        timeSlot={timeSlot}
                        companyId={company.id}
                        key={i}
                        rooms={rooms}
                        eventName={company.compName}
                        eventTitle={company.trainingOccupation}
                      >
                        {meeting?.room?.roomId}
                      </EditableCell>
                    ) : (
                      <TableCell className="p-1 text-center">
                        <Tooltip>
                          <TooltipTrigger asChild className="cursor-help">
                            <FaTimes className="m-auto " />
                          </TooltipTrigger>
                          <TooltipContent side="bottom">
                            <div className="p-2">
                              In diesem Slot findet keine Veranstaltung statt
                            </div>
                          </TooltipContent>
                        </Tooltip>
                      </TableCell>
                    )}
                  </Fragment>
                );
              })
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
