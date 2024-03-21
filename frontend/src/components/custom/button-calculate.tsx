"use client";

import { dataCalculate } from "@/lib/data-calculate";
import { Button } from "../ui/button";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../ui/dialog";
import { toast } from "sonner";
import { useRef, useState } from "react";
import { useRouter } from "next/navigation";

export const ButtonCalculate = (props: { disabled: boolean }) => {
  const [open, setOpen] = useState(false);
  const router = useRouter();
  const onClick = async () => {
    toast.promise(
      dataCalculate().finally(() => {
        router.refresh();
        setOpen(false);
      }),
      {
        loading: "Berechne...",
        success: "Berechnung erfolgreich",
        error: "Berechnung fehlgeschlagen",
      },
    );
  };

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button disabled={props.disabled} type="button">
          Ausrechnen
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle className="text-xl">Auslosung starten</DialogTitle>
        </DialogHeader>
        <p>
          Hier können Sie die <i>Auslosung</i> starten.
          <br />
          Das bedeuted, dass anhand der hochgeladenen Daten die Schüler optimal
          zugeteilt werden.
          <br />
          Sollten die Eingangsdaten späternochmal geändert werden, so müssen Sie
          diese <i>Auslosung</i> hier auch nochmal starten. Darauf wird aber
          auch im späteren Prozess nochmal hingewiesen.
        </p>
        <div className=" text-right text-xs text-green-500">
          Diese Aktion kann später rückgängig gemacht werden.
        </div>
        <DialogFooter>
          <DialogClose asChild>
            <Button variant="secondary">Abbrechen</Button>
          </DialogClose>
          <Button variant="default" onClick={onClick}>
            Starten
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};
