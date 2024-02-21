import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

const Page = () => {
  return (
    <div>
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
              className="opacity-0 h-32 absolute cursor-pointer"
            />
            <Label
              htmlFor="picture"
              className="absolute inset-0 flex justify-center items-center cursor-pointer"
            >
              Excel Datei hier einfügen
            </Label>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default Page;
