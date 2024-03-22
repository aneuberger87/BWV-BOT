import { CardData } from "@/components/custom/card-data";
import { Button } from "@/components/ui/button";
import {
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { getAllRooms } from "@/lib/fetches";
import { FaSquarePlus } from "react-icons/fa6";
import { FaPlus } from "react-icons/fa";
import { AddButton } from "./add-room-button";
import { HelpWrapper } from "@/components/custom/help-wrapper";

const LazyTableBodyCompany = async () => {
  const rooms = await getAllRooms();

  return (
    <TableBody>
      {rooms.roomList
        .sort((a, b) => a.roomId.localeCompare(b.roomId))
        .map((room, i) => (
          <TableRow key={i}>
            <TableCell className="font-medium">{room.roomId}</TableCell>
            <TableCell>{room.capacity}</TableCell>
          </TableRow>
        ))}
    </TableBody>
  );
};

export const PageRooms = () => {
  return (
    <CardData
      hideToggle
      table={{
        header: (
          <TableHeader>
            <TableRow>
              <TableHead>Raum</TableHead>
              <TableHead>Kapazität</TableHead>
            </TableRow>
          </TableHeader>
        ),
        body: <LazyTableBodyCompany />,
      }}
      title="Räume"
      type="roomsList"
    >
      <AddButton />
    </CardData>
  );
};
