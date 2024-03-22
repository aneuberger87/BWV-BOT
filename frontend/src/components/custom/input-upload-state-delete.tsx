"use client";

import { ExcelFileName } from "@/types";
import { Button } from "../ui/button";
import { dataDelete } from "@/lib/data-delete";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { LoadingSpinner } from "./loading-spinner";

export const UploadStateDelete = (props: { type: ExcelFileName }) => {
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const onClick = () => {
    setLoading(true);
    dataDelete(props.type).finally(() => {
      router.refresh();
      setLoading(false);
    });
  };

  return (
    <Button
      variant="destructive"
      type="button"
      onClick={onClick}
      disabled={loading}
    >
      {loading && <LoadingSpinner className="mr-1" />}
      Löschen
    </Button>
  );
};
