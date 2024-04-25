import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Separator } from "../ui/separator";
import InputUploadDefault from "./input-upload-child";
import { InputUploadState } from "./input-upload-state";
import { Suspense } from "react";
import { Skeleton } from "../ui/skeleton";
import { ExcelFileName } from "@/types";
import { excelExists } from "@/lib/excel-exists";

const WrapperInputUploadDefault = async (props: {
  dataValidation: () => Promise<boolean> | boolean;
  type: ExcelFileName;
}) => {
  let isValid = props.dataValidation();
  if (isValid instanceof Promise) {
    isValid = await isValid;
  }
  const exists = excelExists(props.type);
  return <InputUploadDefault initialDisabled={isValid} type={props.type} />;
};

const InputUploadBox = (props: {
  label: string;
  description: string;
  validateFunction: () => Promise<boolean> | boolean;
  dataViewHref: string;
  type: ExcelFileName;
}) => {
  // const upload = async (data: FormData) => {
  //   "use server";
  //   const file: File | null = data.get("file") as unknown as File;
  //   console.log("🚀 ~ upload ~ file:", file);
  //   if (!file) {
  //     throw new Error("No file uploaded");
  //   }

  //   const bytes = await file.arrayBuffer();
  //   const buffer = Buffer.from(bytes);

  //   const path = join("/", "tmp", file.name);
  //   //await writeFile(path, buffer);
  //   console.log(`open ${path} to see the uploaded file`);
  //   redirect("/overview");
  //   revalidatePath("/overview");
  //   return { success: true };
  // };

  return (
    <Card className="min-h-full w-max">
      <form className="w-max">
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
          <InputUploadState
            excelType={props.type}
            targetHraf={props.dataViewHref}
          />
        </CardContent>
      </form>
    </Card>
  );
};

export default InputUploadBox;
