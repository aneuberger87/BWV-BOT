"use client";

import * as React from "react";
import { Check, ChevronsUpDown } from "lucide-react";

import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { RoomList } from "@/types";

export const ComboboxRooms = (props: {
  rooms: RoomList;
  onChange: (value: string) => void;
}) => {
  const list = props.rooms.roomList;
  const [open, setOpen] = React.useState(false);
  const [value, setValue] = React.useState("");

  const onSelect = (currentValue: string) => {
    setValue(currentValue === value ? "" : currentValue);
    setOpen(false);
    props.onChange(currentValue);
  };

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          role="combobox"
          aria-expanded={open}
          className="my-4 justify-between"
        >
          {value
            ? list.find((framework) => framework.roomId === value)?.roomId
            : "Raum auswählen..."}
          <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-[200px] p-0">
        <Command>
          <CommandInput placeholder="Raum suchen..." />
          <CommandEmpty>Kein Raum vorhanden.</CommandEmpty>
          <CommandList>
            <CommandGroup>
              {list
                .sort((a, b) => a.roomId.localeCompare(b.roomId))
                .map((room, i) => (
                  <CommandItem key={i} value={room.roomId} onSelect={onSelect}>
                    <Check
                      className={cn(
                        "mr-2 h-4 w-4",
                        value === room.roomId ? "opacity-100" : "opacity-0",
                      )}
                    />
                    {room.roomId}
                  </CommandItem>
                ))}
            </CommandGroup>
          </CommandList>
        </Command>
      </PopoverContent>
    </Popover>
  );
};
