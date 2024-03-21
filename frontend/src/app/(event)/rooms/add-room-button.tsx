"use client";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { FaPlus } from "react-icons/fa6";

export const AddButton = () => {
  return (
    <Dialog>
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
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Raum hinzufügen</DialogTitle>
        </DialogHeader>
        <form>
          <Input />
          <Input />
        </form>
      </DialogContent>
    </Dialog>
  );
};
