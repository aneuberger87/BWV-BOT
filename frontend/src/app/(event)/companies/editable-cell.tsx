"use client";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { TableCell } from "@/components/ui/table";
import { RoomList } from "@/types";
import { PopoverArrow, PopoverClose } from "@radix-ui/react-popover";
import { useState } from "react";
import { FaCheck, FaTimes } from "react-icons/fa";
import { MdErrorOutline } from "react-icons/md";
import { ComboboxRooms } from "./combobox-rooms";
import { actionRewireRoom } from "./action-rewire-room";
import { useRouter } from "next/navigation";
import { toast } from "sonner";
import { LoadingSpinner } from "@/components/custom/loading-spinner";

export const EditableCell = (props: {
  eventName: string;
  eventTitle: string;
  timeSlot: string;
  companyId: number;
  rooms: RoomList;
  children: React.ReactNode;
}) => {
  const [open, setOpen] = useState(false);
  const [newRoom, setNewRoom] = useState<string>("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    toast.promise(
      actionRewireRoom(`${props.companyId}`, newRoom, props.timeSlot).finally(
        () => {
          router.refresh();
          setOpen(false);
          setNewRoom("");
          setLoading(false);
        },
      ),
      {
        loading: "Raum wird umgelegt...",
        success: "Raum erfolgreich umgelegt",
        error: "Fehler beim umlegen des Raumes",
      },
    );
  };

  console.log(props.children);
  return (
    <TableCell className="p-1 text-center">
      <Popover open={open} onOpenChange={setOpen}>
        <PopoverTrigger asChild>
          <Button
            variant={open ? "secondary" : "ghost"}
            size="icon"
            className={"truncate p-2 text-indigo-700 " + (open ? "border" : "")}
            type="button"
            title={props.eventTitle}
          >
            {!props.children || props.children == "" ? (
              <MdErrorOutline />
            ) : (
              props.children
            )}
          </Button>
        </PopoverTrigger>
        <PopoverContent>
          <PopoverArrow />
          <form onSubmit={onSubmit} className="flex flex-col">
            <h3 className="font-bold">Wähle einen neuen Raum</h3>
            <p className="text-xs">
              <span className="text-red-500">Actung!</span> Sollte der Raum in
              dieser Zeit bereits belegt sein, wird der Raum mit dem bereits
              belegtem Event getauscht.
            </p>
            <ComboboxRooms
              rooms={props.rooms}
              onChange={(e) => setNewRoom(e)}
            />
            <div className="ml-auto mt-2 flex w-max gap-2">
              <PopoverClose asChild>
                <Button variant="outline" size="icon" type="button">
                  <FaTimes />
                </Button>
              </PopoverClose>
              <Button
                variant="outline"
                size="icon"
                type="submit"
                disabled={loading}
              >
                {!loading && <FaCheck />}
                {loading && <LoadingSpinner />}
              </Button>
            </div>
          </form>
        </PopoverContent>
      </Popover>
    </TableCell>
  );
};
