type Method = 'POST' | 'GET' | 'PUT' | 'DELETE';

interface Request {
    bulkId: string;
    method: Method;
    path: string;
    body?: any;
}

interface AssignmentRequest {
    subject: { id: string, subjectType: string };
    role: { code: string };
    primary: boolean;
}

interface MatterData {
    name: string;
    createActivity: boolean;
    typeCode: string;
    description: string;
    finraReceivedDate: string;
    organization: { code: string };
    categories: { code: string }[];
    assignmentRequests: AssignmentRequest[];
}

class DataBuilder {
    private requests: Request[] = [];

    createMatter(data: MatterData): DataBuilder {
        const request: Request = {
            bulkId: 'create-matter',
            method: 'POST',
            path: '/api/v1/matters',
            body: data
        };
        this.requests.push(request);
        return this;
    }

    addOrigin(originId: number): DataBuilder {
        const request: Request = {
            bulkId: 'add-origin-1',
            method: 'POST',
            path: `/api/v1/matters/{bulkId:create-matter}/origins`,
            body: { originId }
        };
        this.requests.push(request);
        return this;
    }

    addCause(causeId: number): DataBuilder {
        const request: Request = {
            bulkId: `add-cause-${this.requests.filter(r => r.bulkId.startsWith('add-cause')).length + 1}`,
            method: 'POST',
            path: '/api/v1/matters/{bulkId:create-matter}/causes',
            body: { codeId: causeId }
        };
        this.requests.push(request);
        return this;
    }

    build(): Request[] {
        return this.requests;
    }
}

// Example usage:
const builder = new DataBuilder();
const matterData: MatterData = {
    name: 'The matter name',
    createActivity: true,
    typeCode: 'REVIEW',
    description: '',
    finraReceivedDate: '2023-10-31',
    organization: { code: 'THE-IRG-TO-BE-DEFINED-ORGANIZATION' },
    categories: [{ code: '20TYPE' }],
    assignmentRequests: [
        { subject: { id: 'K22204', subjectType: 'USER' }, role: { code: 'ANALYST' }, primary: true },
        { subject: { id: 'K22204', subjectType: 'USER' }, role: { code: 'MANAGER' }, primary: true }
    ]
};

const requests = builder.createMatter(matterData)
    .addOrigin(3)
    .addCause(718)
    .addCause(718)
    .build();

console.log(JSON.stringify(requests, null, 2));