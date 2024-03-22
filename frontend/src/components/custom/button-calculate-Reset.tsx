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
import { dataReset } from "@/lib/data-reset";
import { LoadingSpinner } from "./loading-spinner";

export const ButtonCalculateReset = (props: { disabled: boolean }) => {
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const router = useRouter();
  const onClick = async () => {
    setLoading(true);
    toast.promise(
      // TODO: dataCalculateReset
      dataReset().finally(() => {
        router.refresh();
        setOpen(false);
        setLoading(false);
      }),
      {
        loading: "Setze zurück...",
        success: "Zurücksetzung erfolgreich",
        error: "Zurücksetzung fehlgeschlagen",
      },
    );
  };

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button disabled={props.disabled} type="button" variant="default">
          Zurücksetzen
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle className="text-xl">Auslosung zurücksetzen</DialogTitle>
        </DialogHeader>
        <p>
          Hier können Sie die <i>Auslosung</i> zurücksetzen.
          <br />
          Das bedeuted, dass alle generierten Daten gelöscht werden.
          <br />
          Die hochgelandenen Daten bleiben erhalten und können erneut verwendet
          werden.
        </p>
        <div className=" text-right text-xs text-red-500">
          Diese Aktion kann später nicht rückgängig gemacht werden.
        </div>
        <DialogFooter>
          <DialogClose asChild>
            <Button variant="secondary">Abbrechen</Button>
          </DialogClose>
          <Button variant="destructive" onClick={onClick} disabled={loading}>
            {loading && <LoadingSpinner className="pr-1" />}
            Zurücksetzen
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};
