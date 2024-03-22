"use client";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { FaPlus } from "react-icons/fa6";
import { useEffect, useState } from "react";
import { addRoomAction } from "./add-room-action";
import { toast } from "sonner";
import { useRouter } from "next/navigation";
import { LoadingSpinner } from "@/components/custom/loading-spinner";

export const AddButton = () => {
  const [roomNumber, setNumber] = useState("");
  const [roomCapacity, setCapacity] = useState("");
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  useEffect(() => {
    if (!open) {
      setNumber("");
      setCapacity("");
    }
  }, [open]);
  const router = useRouter();
  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    toast.promise(
      addRoomAction({ roomNumber, roomCapacity }).then((res) => {
        if (res.success) {
          setOpen(false);
          setNumber("");
          setCapacity("");
          router.refresh();
          setLoading(false);
        }
      }),
      {
        loading: "Raum wird hinzugefügt...",
        success: "Raum wurde hinzugefügt",
        error: "Fehler beim Hinzufügen des Raumes",
      },
    );
  };
  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button
          className="absolute right-2 top-2 flex gap-2"
          variant="outline"
          size="default"
        >
          <FaPlus />
          <span>Raum hinzufügen</span>
        </Button>
      </DialogTrigger>
      <DialogContent className="w-max">
        <DialogHeader>
          <DialogTitle className="w-max">Raum hinzufügen</DialogTitle>
        </DialogHeader>
        <form className="flex w-max flex-col gap-2" onSubmit={onSubmit}>
          <Label htmlFor="roomNumber" className="mt-2">
            Raumnummer
          </Label>
          <Input
            name="roomNumber"
            type="text"
            required
            className="w-80"
            value={roomNumber}
            onChange={(e) => setNumber(e.target.value)}
          />
          <Label htmlFor="capacity" className="mt-2">
            Kapazität
          </Label>
          <Input
            name="capacity"
            type="number"
            required
            className="w-80"
            value={roomCapacity}
            onChange={(e) => setCapacity(e.target.value)}
          />

          <DialogFooter className="mt-4">
            <Button variant="secondary">Abbrechen</Button>
            <Button type="submit" disabled={loading}>
              {loading && <LoadingSpinner className="mr-1" />}
              Hinzufügen
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
};
