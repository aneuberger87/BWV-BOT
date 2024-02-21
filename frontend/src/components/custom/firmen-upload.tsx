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

const FirmenUpload = () => {
  const upload = async (data: FormData) => {
    "use server";
    console.log(JSON.stringify(data, null, 2));
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
