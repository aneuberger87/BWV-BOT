"use client";

import Link from "next/link";
import { useFormStatus } from "react-dom";
import { FaLink } from "react-icons/fa";
import { Skeleton } from "../ui/skeleton";
import { Suspense } from "react";
import { FaExclamationTriangle } from "react-icons/fa";

export const FormState = async (props: {
  dataIsValid: boolean;
  targetHraf: string;
}) => {
  const { pending } = useFormStatus();

  if (pending) {
    return <Skeleton className="h-8 w-32" />;
  }
  return (
    <Link href={props.targetHraf ?? ""} className="flex items-center gap-1">
      {props.dataIsValid && (
        <>
          <FaLink className="text-sm text-green-500" />{" "}
          <span>Daten sind vorhanden</span>
        </>
      )}
      {!props.dataIsValid && (
        <>
          <FaExclamationTriangle className="text-sm text-red-500" />{" "}
          <span>Daten fehlen</span>
        </>
      )}
    </Link>
  );
};
