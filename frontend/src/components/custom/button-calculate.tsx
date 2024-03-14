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

export const ButtonCalculate = (props: { disabled: boolean }) => {
  const action = async () => {
    "use server";
  };

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button disabled={props.disabled} type="button">
          Ausrechnen
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Auslosung starten</DialogTitle>
        </DialogHeader>
        Hi
        <DialogFooter>
          <DialogClose>
            <Button variant="secondary">Abbrechen</Button>
          </DialogClose>
          <Button variant="default">Starten</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};
