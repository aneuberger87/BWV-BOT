import { Button } from "../ui/button";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../ui/dialog";
import { Separator } from "../ui/separator";
import { Badge } from "../ui/badge";
import { FaPrint } from "react-icons/fa6";

const SubHeadiong = (props: { children: React.ReactNode }) => {
  return <h3 className="text-lg">{props.children}</h3>;
};

export const ButtonPrint = () => {
  const SeperatorSpan = () => <Separator className="col-span-2" />;
  const VerlosungDestructive = () => (
    <Badge variant="destructive" className="w-max text-xs font-light">
      Verlosung
    </Badge>
  );
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="secondary">Drucken</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Event Ausdrucke</DialogTitle>
          <DialogDescription>
            Hier können Sie verschiedene Drucke auslösen.
            <br />
            Einige Drucke sind erst nach der Auslosung verfügbar.
          </DialogDescription>
        </DialogHeader>
        <div className="grid grid-cols-2 gap-4">
          <SubHeadiong>
            Aufteilung <VerlosungDestructive />
          </SubHeadiong>
          <Button variant="ghost" disabled>
            <FaPrint />
          </Button>
          <SeperatorSpan />
          <SubHeadiong>
            Laufzettel <VerlosungDestructive />
          </SubHeadiong>
          <Button variant="ghost" disabled>
            <FaPrint />
          </Button>
          <SeperatorSpan />
          <SubHeadiong>Raumplan</SubHeadiong>
          <Button variant="ghost">
            <FaPrint />
          </Button>
          <SeperatorSpan />
          <SubHeadiong>
            Anwesenheit <VerlosungDestructive />
          </SubHeadiong>
          <Button variant="ghost" disabled>
            <FaPrint />
          </Button>
        </div>
      </DialogContent>
    </Dialog>
  );
  //   return (
  //     <Popover>
  //       <PopoverTrigger asChild>
  //         <Button variant="secondary">Drucken</Button>
  //       </PopoverTrigger>
  //       <PopoverContent side="right" align="end">
  //         <Button>Test</Button>
  //       </PopoverContent>
  //     </Popover>
  //   );
};
