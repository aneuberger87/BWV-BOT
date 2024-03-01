import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { writeFile } from "fs/promises";
import { join } from "path";
import { Separator } from "../ui/separator";
import InputUploadDefault from "./input-upload-default";
import { FormState } from "./form-state";
import { Suspense } from "react";
import { Skeleton } from "../ui/skeleton";
import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";

const WrapperFormState = async (props: {
  dataValidation: () => Promise<boolean> | boolean;
  targetHraf: string;
}) => {
  let isValid = props.dataValidation();
  if (isValid instanceof Promise) {
    isValid = await isValid;
  }
  return <FormState dataIsValid={isValid} targetHraf={props.targetHraf} />;
};

const WrapperInputUploadDefault = async (props: {
  dataValidation: () => Promise<boolean> | boolean;
  type: "studentsList" | "roomsList" | "companiesList";
}) => {
  let isValid = props.dataValidation();
  if (isValid instanceof Promise) {
    isValid = await isValid;
  }

  return <InputUploadDefault initialDisabled={isValid} type={props.type} />;
};

const InputUploadBox = (props: {
  label: string;
  description: string;
  validateFunction: () => Promise<boolean> | boolean;
  dataViewHref: string;
  type: "studentsList" | "roomsList" | "companiesList";
}) => {
  const upload = async (data: FormData) => {
    "use server";
    const file: File | null = data.get("file") as unknown as File;
    console.log("🚀 ~ upload ~ file:", file);
    if (!file) {
      throw new Error("No file uploaded");
    }

    const bytes = await file.arrayBuffer();
    const buffer = Buffer.from(bytes);

    const path = join("/", "tmp", file.name);
    //await writeFile(path, buffer);
    console.log(`open ${path} to see the uploaded file`);
    redirect("/overview");
    revalidatePath("/overview");
    return { success: true };
  };

  return (
    <form action={upload}>
      <Card className="w-max">
        <CardHeader>
          <CardTitle>{props.label}</CardTitle>
          <CardDescription>{props.description}</CardDescription>
        </CardHeader>
        <CardContent className="">
          <Suspense fallback={<Skeleton className="h-32 w-72" />}>
            <WrapperInputUploadDefault
              dataValidation={props.validateFunction}
              type={props.type}
            />
          </Suspense>
          <Separator orientation="horizontal" className="mb-2 mt-4 w-full" />
          <Suspense fallback={<Skeleton className="h-6 w-48 " />}>
            <WrapperFormState
              dataValidation={props.validateFunction}
              targetHraf={props.dataViewHref}
            />
          </Suspense>
        </CardContent>
      </Card>
    </form>
  );
};

export default InputUploadBox;
