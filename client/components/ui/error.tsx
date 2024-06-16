import { Alert, AlertDescription, AlertTitle } from "./alert";

const Error = ({ title, message }: { title: string; message: string }) => {
  return (
    <div className="p-4">
      <Alert variant="destructive" className="p-6 w-full">
        {/* <Terminal className="h-4 w-4" /> */}
        <AlertTitle>{title}</AlertTitle>
        <AlertDescription>{message}</AlertDescription>
      </Alert>
    </div>
  );
};

export default Error;
