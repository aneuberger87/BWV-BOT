import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "../ui/button";
import { join } from "path";
import { writeFile } from "fs/promises";

const FirmenUpload = () => {
  const upload = async (data: FormData) => {
    "use server";
    const file: File | null = data.get("file") as unknown as File;
    if (!file) {
      throw new Error("No file uploaded");
    }

    const bytes = await file.arrayBuffer();
    const buffer = Buffer.from(bytes);

    const path = join("/", "tmp", file.name);
    await writeFile(path, buffer);
    console.log(`open ${path} to see the uploaded file`);

    return { success: true };
  };

  return (
    <form action={upload}>
      <Card className="w-max">
        <CardHeader>
          <CardTitle>Firmenliste hochladen</CardTitle>
          <CardDescription>Page description</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="relative h-32 border rounded cursor-pointer">
            <Input
              id="picture"
              type="file"
              className=" h-32 absolute cursor-pointer"
              name="file"
            />
            <Label
              htmlFor="picture"
              className="absolute inset-0 flex justify-center items-center cursor-pointer"
            >
              Excel Datei hier einfügen
            </Label>
          </div>
          <Button>Upload</Button>
        </CardContent>
      </Card>
    </form>
  );
};

export default FirmenUpload;
