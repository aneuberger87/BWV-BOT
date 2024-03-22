"use client";

import { Button } from "@/components/ui/button";
import { FaDownload } from "react-icons/fa6";
import { toast } from "sonner";

export const Download = (props: {
  title: string;
  type: "attendence-list" | "room-assignment-list" | "timetable-list";
  id: string;
}) => {
  const niceName =
    props.type == "attendence-list"
      ? "Anwesenheitslisten"
      : props.type == "room-assignment-list"
        ? "Raumaufteilungsliste"
        : "Laufzettel";
  const url = `/api/calculated/${props.type}`;

  const onClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();

    fetch(url)
      .then((response) => {
        if (response.ok) {
          response.blob().then((blob) => {
            const newUrl = window.URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.href = newUrl;
            link.setAttribute("download", `${niceName}.xlsx`);
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
          });
        } else {
          toast.error(
            "An error occurred while downloading the file " +
              props.type +
              ".xlsx.",
          );
        }
      })
      .catch((error) => {
        console.error("Fetch error: ", error);
        toast.error("An error occurred while downloading the file.");
      });
  };

  return (
    <Button variant="secondary" className="flex-grow" onClick={onClick} asChild>
      <a href={url} download={`${props.type}.xlsx`} id={props.id}>
        <FaDownload className="mr-4" />
        {props.title}
      </a>
    </Button>
  );
};
