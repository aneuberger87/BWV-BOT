import React from "react";
import { FaDownload, FaQuestion } from "react-icons/fa6";
import { Button } from "../ui/button";
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "../ui/sheet";
import { ScrollArea } from "../ui/scroll-area";

export const HelpWrapper = (Props: {
  helpTitle: string;
  helpDescription?: string;
  helpContent: React.ReactNode;
  helpFooter?: React.ReactNode;
  helpHoverText?: string;
}) => {
  return (
    <Sheet>
      <SheetTrigger asChild>
        <Button size="icon" variant="outline" type="button">
          <FaQuestion />
        </Button>
      </SheetTrigger>
      <SheetContent className="grid grid-rows-[auto_1fr_auto]">
        <SheetHeader>
          <SheetTitle>{Props.helpTitle}</SheetTitle>
          <SheetDescription>{Props.helpDescription}</SheetDescription>
        </SheetHeader>
        <div className="mt-6">
          <ScrollArea className="h-0 min-h-full">
            {Props.helpContent}
          </ScrollArea>
        </div>
        <SheetFooter className="mt-auto">
          {Props.helpFooter}
          <Button variant="secondary">
            <FaDownload className="mr-4" />
            Benutzerdokumentation herunterladen
          </Button>
        </SheetFooter>
      </SheetContent>
    </Sheet>
  );
};
