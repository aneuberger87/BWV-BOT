import { CardData } from "@/components/custom/card-data";
import {
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { getAllRooms } from "@/lib/fetches";

const LazyTableBodyCompany = async () => {
  const rooms = await getAllRooms();

  return (
    <TableBody>
      {rooms.roomList.map((room, i) => (
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
    />
  );
};
