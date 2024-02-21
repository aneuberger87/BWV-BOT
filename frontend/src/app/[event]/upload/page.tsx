import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

const UploadPaged = () => {
  return (
    <div className="grid w-full max-w-sm items-center gap-1.5">
      <Label htmlFor="excel">Excel</Label>
      <Input id="excel" type="file" />
    </div>
  );
};

export default UploadPaged;
