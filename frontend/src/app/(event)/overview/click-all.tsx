"use client";

import { Button } from "@/components/ui/button";
import { FaDownload } from "react-icons/fa6";

export const ClickAll = (props: { idsToClick: string[] }) => {
  const onClick = () => {
    props.idsToClick.forEach((id) => {
      const element = document.getElementById(id);
      if (element) {
        element.click();
      }
    });
  };
  return (
    <Button variant="secondary" className="mt-4 flex-grow" onClick={onClick}>
      <FaDownload className="mr-4" /> Alle Excel-Dateien herunterladen
    </Button>
  );
};
