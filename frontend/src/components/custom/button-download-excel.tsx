"use client";
import React from "react";
import { Button } from "../ui/button";
import { FaFileDownload } from "react-icons/fa";
import { ExcelFileName } from "@/types";
import { download } from "@/lib/action-download";
import { excelFileName } from "@/lib/excel-file-name";

const ButtonDownloadExcel = (props: { type: ExcelFileName }) => {
  const handleDownload = async () => {
    const fileContent = await download(props.type); // Call the download action
    if (fileContent.file === null) return;
    const byteCharacters = atob(fileContent.file);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
      byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);
    const blob = new Blob([byteArray], {
      type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    });
    // Create a link element to facilitate downloading
    const link = document.createElement("a");
    link.download = excelFileName(props.type);
    link.href = window.URL.createObjectURL(blob);
    document.body.appendChild(link); // Append to the document
    link.click(); // Programmatically click the link to trigger the download

    // Clean up by removing the link element
    document.body.removeChild(link);
  };

  const url =
    props.type === "companiesList"
      ? "/api/download-companies"
      : props.type === "studentsList"
        ? "/api/download-students"
        : "/api/download-rooms";

  return (
    <Button size="icon" variant="outline" type="button" asChild>
      <a href={url} download={excelFileName(props.type)}>
        <FaFileDownload />
      </a>
    </Button> // Button element to trigger download
  );
};

export default ButtonDownloadExcel;
