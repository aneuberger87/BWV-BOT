import { Button } from "../ui/button";
import { Input } from "../ui/input";
import { Label } from "../ui/label";
import { FaQuestion, FaCheck } from "react-icons/fa";

export const UploadInline = (props: { label: string; id: string }) => {
  return (
    <form className="flex gap-2 items-end">
      <div className="grid w-full max-w-sm items-center gap-1.5">
        <Label htmlFor={props.id}>{props.label}</Label>
        <Input id={props.id} type="file" />
      </div>
      <Button variant="outline" size="icon" title="Upload" type="submit">
        <FaCheck className="text-lg" />
      </Button>
      <Button variant="outline" size="icon" className="ml-2" type="button">
        <FaQuestion className="text-lg" />
      </Button>
    </form>
  );
};
