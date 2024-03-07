"use client";

import { ExcelFileName } from "@/types";
import { Button } from "../ui/button";
import { deleteData } from "@/lib/action-delete-data";
import { useRouter } from "next/navigation";

export const UploadStateDelete = (props: { type: ExcelFileName }) => {
  const router = useRouter();
  const onClick = () => {
    deleteData(props.type);
    router.refresh();
  };

  return (
    <Button variant="destructive" type="button" onClick={onClick}>
      Löschen
    </Button>
  );
};
