"use client";

import { cn } from "@/lib/utils";
import { useCallback, useMemo, useRef, useState } from "react";
import { useFormStatus } from "react-dom";
import { useDropzone } from "react-dropzone";
import { upload } from "../../lib/action-upload";
import { toast } from "sonner";
import { useRouter } from "next/navigation";

const InputUploadDefault = (props: {
  initialDisabled?: boolean;
  type: "studentsList" | "roomsList" | "companiesList";
}) => {
  const router = useRouter();
  const [file, setFile] = useState<File | null>(null); // State to track a single uploaded file
  const [directUploadPending, setDirectUploadPending] = useState(false); // State to track direct upload status
  const { pending } = useFormStatus();
  const inputRef = useRef<HTMLInputElement>(null);

  const hasFile = file !== null;

  const onDrop = useCallback((acceptedFiles: File[]) => {
    // Ensure there's at least one file
    if (acceptedFiles.length === 0 || acceptedFiles.length > 1) return;
    const fileExtension = acceptedFiles[0].name.split(".").pop();
    if (fileExtension !== "xlsx" && fileExtension !== "xls") {
      toast.error("Nur .xlsx und .xls Dateien sind erlaubt");
      return;
    }

    const file = acceptedFiles[0];
    setDirectUploadPending(true);
    setFile(file);

    const reader = new FileReader();
    reader.onloadend = () => {
      // Convert file content to a Base64 string
      const base64String = reader.result as string;

      const data = {
        type: props.type,
        fileBase64: base64String,
      };

      // Now you can call your upload Server Action with the base64String
      upload(data).then(() => {
        setDirectUploadPending(false);
        if (inputRef.current) {
          inputRef.current.value = "";
        }
        router.refresh();
      });
    };
    reader.readAsDataURL(file);
  }, []);
  const {
    getRootProps,
    getInputProps,
    isDragActive,
    isFocused,
    isDragAccept,
    isDragReject,
  } = useDropzone({ onDrop, maxFiles: 1 });

  let className =
    "flex max-h-32 flex-col cursor-pointer items-center text-center justify-center p-5 border-2 rounded border-dashed border-gray-300 bg-primary-foreground text-gray-400 outline-none transition-colors duration-200 ease-in-out  ";

  if (props.initialDisabled && !hasFile) {
    className += "opacity-50 relative";
  }

  // Dynamic Tailwind classes for different states
  const focusedClasses = "border-blue-500";
  const acceptClasses = "border-green-500";
  const rejectClasses = "border-red-500";

  // Combine base with conditional classes
  const combinedClasses = useMemo(() => {
    let classes = className;
    if (isFocused) classes = cn(classes, focusedClasses);
    if (isDragAccept) classes = cn(classes, acceptClasses);
    if (isDragReject) classes = cn(classes, rejectClasses);
    return classes;
  }, [isFocused, isDragAccept, isDragReject, className]);

  return (
    <div className="relative grid h-36 min-h-max w-72 grid-rows-[1fr_auto]">
      <div {...getRootProps({ className: combinedClasses })}>
        <input
          {...getInputProps()}
          name="file"
          ref={inputRef}
          accept=".xlsx, .xls"
        />
        {isDragActive ? (
          <p>Lassen Sie die Datei fallen.</p>
        ) : (
          <p>
            {file ? (
              <>
                <span>
                  Geladene Datei:
                  <br />
                  {file.name}
                </span>
              </>
            ) : (
              <>
                Ziehen Sie eine Datei hierher <br />
                oder klicken Sie, um eine Datei auszuwählen.
              </>
            )}
          </p>
        )}
        {props.initialDisabled && !hasFile && !directUploadPending && (
          <div className="absolute inset-0 flex items-center justify-center bg-primary-foreground ">
            <span>Daten überschreiben</span>
          </div>
        )}
        {directUploadPending && (
          <div className="absolute inset-0 flex items-center justify-center bg-primary-foreground">
            <span>Wird hochgeladen...</span>
          </div>
        )}
      </div>
      {hasFile && !directUploadPending && (
        <div className="pt-4">
          <p className="font-mono">Geladen: {file.name}</p>
        </div>
      )}
      {hasFile && directUploadPending && (
        <div className="pt-4">
          <p className="font-mono">{file.name}</p>
        </div>
      )}
    </div>
  );
};

export default InputUploadDefault;
