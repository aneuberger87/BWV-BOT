import { excelExists } from "@/lib/excel-exists";
import { ExcelFileName } from "@/types";
import Link from "next/link";
import {
  FaExclamationTriangle,
  FaExternalLinkSquareAlt,
  FaLink,
} from "react-icons/fa";
import { MdDeleteForever } from "react-icons/md";
import { Button } from "../ui/button";
import ButtonDownloadExcel from "./button-download-excel";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../ui/dialog";
import { excelFileName } from "@/lib/excel-file-name";
import { UploadStateDelete } from "./input-upload-state-delete";

const DeleteButton = (props: { type: ExcelFileName }) => {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline" size="icon">
          <MdDeleteForever className="text-xl" />
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle className="text-2xl">Daten Löschen</DialogTitle>
        </DialogHeader>
        <p>
          Möchten Sie die Datei <b>{excelFileName(props.type)}</b> wirklich
          löschen?
          <br />
          Das wird ebenfalls alle Daten löschen, die sich auf diese Datei
          beziehen oder auf Basis dieser Datei generiert wurden.
          <br />
        </p>
        <div className=" text-right text-xs text-red-500">
          Diese Aktion kann nicht rückgängig gemacht werden.
        </div>
        <DialogFooter>
          <UploadStateDelete type={props.type} />
          <DialogClose asChild>
            <Button variant="secondary">Abbrechen</Button>
          </DialogClose>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};

export const InputUploadState = async (props: {
  excelType: ExcelFileName;
  targetHraf: string;
}) => {
  const exists = excelExists(props.excelType);
  return (
    <>
      {exists && (
        <div className="flex items-center justify-between gap-1">
          <FaLink className="text-sm text-green-500" />{" "}
          <span className="cursor-default">Daten vorhanden </span>
          <Button variant="outline" size="icon" asChild>
            <Link
              href={props.targetHraf ?? ""}
              className="flex items-center gap-1"
            >
              <FaExternalLinkSquareAlt />
            </Link>
          </Button>
          <DeleteButton type={props.excelType} />
          <ButtonDownloadExcel type={props.excelType} />
        </div>
      )}
      {!exists && (
        <div className="flex cursor-default items-center gap-1">
          <FaExclamationTriangle className="text-sm text-red-500" />{" "}
          <span>Daten fehlen</span>
        </div>
      )}
    </>
  );
};
